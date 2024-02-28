"""
1) Reads through a WSRMac, collects all SpeechBird COMMAND_INFO blocks and MANUAL_SECTION titles.
2) Outputs HTML listing all the commands and their details.

Expected Manual Section format:
    <!-- 	MANUAL_SECTION: 1. Typing Enhancements -->


Expected infoblock format:
    <!--
        COMMAND_INFO_START
        ToDo:	Required, string (eg "Press up arrow")
        Say:	Required, string (eg "Up")
        Detail:	Optional, string (eg "Add 's' to select, eg 'ups')
        Attrib:	Optional, list of key:value pairs, boolean. 1 if listed, 0 if not: Advanced, Streamable, Selecting, Multiplier, Moused, Ordinal
        COMMAND_INFO_END
    -->
"""

import sys
import re

def parse_wsr_mac(xml_file):
    with open(xml_file, 'r', encoding='utf-16-le') as file:
        lines = file.readlines()

    commands = {}
    current_topic = None

    # Initialize variables to store command information
    todo, say, detail, attrib = '', '', '', ''
    in_info_block = False

    # Regular expressions to match start and end of COMMAND_INFO block
    start_pattern = re.compile(r'\s*COMMAND_INFO_START\s*')
    end_pattern = re.compile(r'\s*COMMAND_INFO_END\s*')
    topic_pattern = re.compile(r'<!--\s*MANUAL_SECTION:\s*(.*)\s*-->')

    # Process each line in the file
    for line in lines:
        # Check if we are in a COMMAND_INFO block
        if start_pattern.match(line):
            in_info_block = True
            continue

        if end_pattern.match(line):
            in_info_block = False
            # Append the extracted command information to the current topic
            if current_topic:
                commands[current_topic].append({
                    'ToDo': todo.strip(),
                    'Say': say.strip(),
                    'Detail': detail.strip(),
                    'Attrib': attrib.strip()
                })
                # DEBUG print(f"Added:\n{commands[current_topic]}")
            # Reset variables for next command
            todo, say, detail, attrib = '', '', '', ''
            continue

        # Check if a new topic is starting
        topic_match = topic_pattern.match(line)
        
        if topic_match:
            # DEBUG print(f"Found topic {topic_match.group(1)}")
            current_topic = topic_match.group(1)
            commands[current_topic] = []
            continue

        # Extract information within COMMAND_INFO block
        if in_info_block:
            if 'ToDo:' in line:
                todo = line.split(':', 1)[1].strip()
            elif 'Say:' in line:
                say = line.split(':', 1)[1].strip()
            elif 'Detail:' in line:
                detail = line.split(':', 1)[1].strip()
            elif 'Attrib:' in line:
                attrib = line.split(':', 1)[1].strip()

    return commands

def generate_topic_list(commands):
    topic_list = '<ul>\n'
    for topic in commands.keys():
        topic_list += f'<li><a href="#{topic.replace(" ", "_")}">{topic}</a></li>\n'
    topic_list += '</ul>\n'
    return topic_list

# Basic HTML Table
# def generate_command_table(topic, commands):
#     html_table = f'<h2 id="{topic.replace(" ", "_")}">{topic}</h2>\n'
#     html_table += '<table border="1">\n'
#     html_table += '<tr><th>ToDo</th><th>Say</th><th>Detail</th><th>Attrib</th></tr>\n'

#     for command in commands:
#         html_table += f'<tr><td>{command["ToDo"]}</td><td>{command["Say"]}</td><td>{command["Detail"]}</td><td>{command["Attrib"]}</td></tr>\n'

#     html_table += '</table>\n'
#     return html_table

# Use Bootstrap's prettier table format
def generate_command_table(topic, commands):
    html_table = f'<h2 id="{topic.replace(" ", "_")}">{topic}</h2>\n'
    html_table += '<table class="table table-striped">\n'
    html_table += '<thead><tr><th>To Do...</th><th>You Say...</th><th>Details</th><th>Attributes</th></tr></thead>\n'
    html_table += '<tbody class="table-striped">\n'

    for command in commands:
        html_table += f'<tr><td>{command["ToDo"]}</td><td>{command["Say"]}</td><td>{command["Detail"]}</td><td>{command["Attrib"]}</td></tr>\n'

    html_table += '</tbody></table>\n'
    return html_table


# Table of Contents at head of single iframe
# def generate_html(commands):
#     html = generate_topic_list(commands)
#     for topic, topic_commands in commands.items():
#         html += generate_command_table(topic, topic_commands)
#     return html

# iframe on left for TOC, wide iframe on right for content
def generate_html(commands):
    toc = generate_topic_list(commands)
    content = ""
    for topic, topic_commands in commands.items():
        content += generate_command_table(topic, topic_commands)

    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ margin: 0; padding: 0; }}
            #menu {{ position: fixed; top: 0; left: 0; width: 20%; height: 100vh; overflow-y: scroll; }}
            #content {{ position: absolute; top: 0; left: 20%; width: 80%; height: 100vh; overflow-y: scroll; }}
        </style>
    </head>
    <body>
        <div id="menu">
            {toc}
        </div>
        <div id="content">
            {content}
        </div>
    </body>
    </html>
    '''

    return html


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py input.WSRMac")
        sys.exit(1)

    xml_file = sys.argv[1]
    commands = parse_wsr_mac(xml_file)
    html = generate_html(commands)

    # Writing the HTML to a file
    with open('../speechbird_commands.html', 'w') as file:
        file.write(html)

if __name__ == "__main__":
    main()

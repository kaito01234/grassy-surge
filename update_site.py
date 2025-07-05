#!/usr/bin/env python3

import datetime
from html.parser import HTMLParser

class TimestampUpdater(HTMLParser):
    def __init__(self, new_timestamp):
        super().__init__()
        self.new_timestamp = new_timestamp
        self.output = []
        self.in_timestamp = False
        
    def handle_starttag(self, tag, attrs):
        attrs_str = ''.join(f' {k}="{v}"' for k, v in attrs)
        self.output.append(f'<{tag}{attrs_str}>')
        
        if tag == 'span' and ('class', 'timestamp') in attrs:
            self.in_timestamp = True
    
    def handle_endtag(self, tag):
        self.output.append(f'</{tag}>')
        if tag == 'span' and self.in_timestamp:
            self.in_timestamp = False
    
    def handle_data(self, data):
        if self.in_timestamp:
            self.output.append(self.new_timestamp)
        else:
            self.output.append(data)
    
    def get_result(self):
        return ''.join(self.output)

def update_html():
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    try:
        with open('templates/index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        parser = TimestampUpdater(current_time)
        parser.feed(html_content)
        updated_content = parser.get_result()
        
        with open('templates/index.html', 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        return current_time
    except FileNotFoundError:
        print("templates/index.html not found")
        return None

def main():
    print("Site update started")
    
    current_time = update_html()
    if current_time:
        print(f"Timestamp updated to: {current_time}")
    else:
        print("Update failed")
    
    print("Site update completed")

if __name__ == '__main__':
    main()
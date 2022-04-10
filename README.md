# SuperPutty Sessions.XMLto Hosts Converter
The sessions.xml file that my team uses has 1400 entries! Kinda insane. This little script converts SuperPutty sessions.xml file into output that can be copy/pasted into hosts file. I needed a way to quickly copy content from the sessions file into a hosts file so that I can automate some of the configuration using Ansible (DNS is not an option in my environment)

## Usage

```bash
python SuperPuttySessionsXMLtoHostsConverter.py
```
The above script assumes that the SuperPutty sessions.xml file is in the same directory as the script. Outputs hosts.txt and also prints output, so you can copy/paste output from either source into your hosts file.

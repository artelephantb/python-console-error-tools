# Console Error Tools
A set of console error tools for python! (No credit required)

## Usage
### Finish
Shows a final message and exits the program
```python
finish('Packaged Project', 'Successfully compiled project into a package', hint='Output at ../data/output/')
```
### Note
Shows a general message
```python
note('Not Production', 'Server in debug mode, not for production', hint='Disable debug mode at ../project/settings.yml')
```
### Warning
Shows a warning message
```python
warning('Too Mutch Data', 'Data is reaching max capacity', hint='Type %8 to max out overflow')
```
### Fumble
Shows a error message without exiting the program
```python
fumble('Sync Error', 'Unable to sync with cloud', hint='Restart network connection')
```
### Error
Shows a error message and exits the program
```python
error('File Exists', 'File existant at ../data/output/text.txt', hint='Remove obstruction')
```

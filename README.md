# Lotsa_Fun_Included
 Lotsa_Fun_Included is an ultra light weight Python tool used to search Linux servers for fun files using [Local File Inclusion](https://en.wikipedia.org/wiki/File_inclusion_vulnerability#Local_file_inclusion) bugs.
 
## Why
Because there's no really good, simple to use, Local File Inclusion testing tools out there.

## How
Python + [Python Requests](https://requests.readthedocs.io/en/master/) + A giant word list of interesting Linux files.

## Usage

`python lotsa_fun_included.py`

```
  --url
        The full LFI vulnerable endpoint ( All "../../../" included )
  --wordlist
        The file name of a custom word list. Not Required.
  --debug
        This flag sets the output to debug.
```

## Future Plans
* Providing educational knowledge when fun files are found using this script. (What the file is, what you can / might learn from it, etc)
* Multithreaded
* Saving the results as it goes in case of crash or system restart.

## Pull Requests
Love em'! Send em' over and I'll review / merge!
# English word learning assistant using Oxford Dictionaries (Python 3)
This program allows you to define a list of words for which pronounciations, definitions, examples and etymologies will be fetched from the Oxford Dictionaries API and displayed in a compact and convenient manner, perfect for studying a large collection of new words. 

## Features
* Display definitions, examples, pronounciations and etymologies for an user-defined list of words
* Simple and concice plain-text output
* Words are processed in order, but can individually be 'dismissed' to push them to the end in the output file
* The input word list supports comments, which can optionally be displayed in the output file
* Word caching support for Enterprise licence holders (see Requirements)


# Requirements
1. Python 3 with 'requests' module (can be installed using "pip install requests")
2. Oxford Dictionaries API access. A free account (the 'Prototype' plan) can be created at https://developer.oxforddictionaries.com.
	The prototype plan allows for up to 1000 free API requests per month and has a rate limit of 60 requests per minute. 
	
	<i>This program also supports word caching to minimize API requests if different outputs are wanted for the same words (e.g reordering, commenting-uncommenting, dismissing), however it is important to note that this functionality is only available to 'Enterprise' plan users as per the Oxford Dictionaries API TOS section 6 (https://developer.oxforddictionaries.com/api-terms-and-conditions).</i>


# Usage
1. Copy "oxford_dicts_config.default.py" to "oxford_dicts_config.py"
2. Create a new app on the Oxford Dictionaries website
3. Replace your app's Application ID and keys into the config file "oxford_dicts_config.py".
	* Change any config values as necessary (before running the program)
4. Use "python dict.py --help" to list command line options
	* When the program is called with no arguments given, default file paths are used


# Examples

## Example input
* See 'in_words.README.txt' for examples and explainations of supported syntax (the file itself can be processed by the program)
* See 'in_words.txt' for a real-world example word list


## Example output
Here is an example of how output for a word might be formatted:

```
<word>
https://www.lexico.com/en/definition/<word>
Verb: <IPA pronounciation>
	DEF: <definition 1>
			<example>
			<example>
	DEF: <definition 2>
			<example>
		DEF: <subdefinition 2.1>
				<example>

	Etymologies:
		<word etymology 1>
		<word etymology 2>

Adjective:<IPA pronounciation>
	DEF: <definition 1>
			<example>
```
			
All (uncommented) words from the input file will be listed in the output file. The output for a word depends on what content is available.

If there are multiple lexical entries (like 2 in the above example for 'verb' and 'adjective') all of them will be shown. For each lexical entry, all definitions, appliccable examples, word etymology and IPA pronounciation will be shown. There is also a link to lexico.com for every word for additional info.
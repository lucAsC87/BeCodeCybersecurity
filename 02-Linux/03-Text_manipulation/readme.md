# Text manipulation with Linux

- Type of Challenge: `Learning` 
- Duration: `1 day`
- Aim - `Learning and application`
- Challenge type : `solo`

Connect to the virtual machine 10.12.x.x with the following credentials:

* **ip** : 10.12.x.x 
* **user** : Name
* **password** : name

## Advanced commands (tail -f, grep, cut, wc, sort, uniq, sed, awk...)
When you work with linux a graphical user interface is not always available. In most cases, you'll just have the access to a terminal of a remote machine, on which you have just logged in using ssh. It is therefore interesting to be able to use specific commands to easily find a file, folder or even search for pieces of text in files. This is what we will do here. 

### cat

``cat`` is an essential tool that displays the content of one or more text files.

````sh
$ cat file.txt
````

So you can concatenate files in this way:

````sh
$ cat file1.txt file2.txt file3.txt > concatenation.txt

````

### more, less 
More and less are interactive commands not to be used in a script. They allow to display a text file, to move, to search etc... more does not allow to go back while less does.
````sh
$ less long-text.txt
````

### tail and head
tail displays the last N lines of a content and head displays the first N lines of a content. N being a parameter.

````sh
# display the last 2 lines of file.txt
$ tail -n 2 file.txt

# displays the first 2 lines of file.txt
$ head -n 2 file.txt

# displays the third and fourth line of file.txt
$ head -n 4 file.txt | tail -n 2
# is equivalent to
$ cat file.txt | head -n 4 | tail -n 2

# display a file from the second line
$ tail -n +2 file.txt
````

### Watch
The watch command runs a command at regular intervals and displays its result. This can be useful, for example, to observe the evolution of the size of a file:
````sh
$ watch du -sh my_file.txt
````
It can also be used to check in real time the appearance of result files:

````sh
$ watch ls my_result_folder
````

### Split
Split a file into several sub-files.

````sh
$ split -b 1024k my_big_file

````
Split will create files named xaa, xab, xac[, etc], with sizes equal or smaller (for the last one) than 1024 Kb.

````sh
$ split -n 10 my_big_file

````
Split will produce here 10 files

````sh
$ split -l 4 my_big_file
````
Split will create files with sizes equal to or smaller (for the last one) than 4 lines.

### Join
Allows to merge the lines of two files having common fields (by default the first column)

````sh
$ cat  testfile1
1 India
2 US
3 Ireland
4 UK
5 Canada

$ cat testfile2
1 NewDelhi
2 Washington
3 Dublin
4 London
5 Toronto

$ join testfile1 testfile2
1 India NewDelhi
2 US Washington
3 Ireland Dublin
4 UK London
5 Canada Toronto
````

### Paste
The paste command allows you to concatenate the lines of the files passed as arguments.

````sh
$ cat  testfile1
1 India
2 US
3 Ireland
4 UK
5 Canada

$ cat testfile2
1 NewDelhi
2 Washington
3 Dublin
4 London
5 Toronto

$ paste testfile1 testfile2
1 India 1 NewDelhi
2 US    2 Washington
3 Ireland   3 Dublin
4 UK    4 London
5 Canada    5 Toronto

````

## Text patterns (regular expressions and wildcards)
Text patterns are a notation that allows to express in a clear, unambiguous and concise way one or more strings of characters. This notation takes several forms depending on the context in which it is used. In theory it allows to express all possible and imaginable strings and groups of strings. These patterns can be very simple and very complicated. These patterns will be very useful for :

- file or string search
- replacing complex patterns
- handling several files at the same time (a regular expression is enough to express several file names at once)

A lot of information about wildcards and regular expressions are summarized in the LPI training courses: https://learning.lpi.org/en/learning-materials/101-500/103/103.3/103.3_01/ On this page you can also find documentation that covers BASH, awk, sed, rights, search etc...


### Wildcards 
Wildcards are a limited and syntactically shorter version of regular expressions.


When we write a regular expression in BASH to express file names, we are talking about wildcards or jokers. The logic is the same as for extended regular expressions but the expression power is less. An important character is '*' . It means any character, zero, one or more times. We can also say 'any string'.

Some examples:

````sh
# list the files whose name ends with ".txt
ls *.txt

# list files/directories whose name starts with "my
ls my*

# list files/directories whose name contains "my
ls *my*

# list files/directories whose name does not start with 'a
ls [^a]*
````

### Regular expressions
Much more complete than wildcards, regular expressions (also called regular expressions or "regex(p)" for short) are used in tools like sed, awk, grep and in many languages... Regular expressions are mainly divided into 3 categories: BRE (basic regular expression), ERE (extended regular expression) and PCRE (Perl Compatible Regular Expressions). All expressions written in basic form (BRE) can be understood by the other forms. PCRE is the most complete implementation. The difference between ERE and BRE is small; here is an extract from wikipedia:

> ERE adds ?, +, and |, and it removes the need to escape the metacharacters ( ) and { }, which are required in BRE

All about regular expressions: http://www.grymoire.com/Unix/Regular.html Or wikipedia: http://en.wikipedia.org/wiki/Regular_expression

Major difference with wildcards, for example on the '*' character. It means here: the previous character repeated zero, one or more times.

To know more about regexp LPI training link.

**Metacharacters**  
A string to search for will be called a pattern. There are several ways to build a pattern. The more precise you are, the less likely it is that another similar string will be found.

All the special characters that follow are called metacharacters. In order to avoid that they are interpreted, you must, +depending on the context, "escape" them with the symbol "\" or use apostrophes (')+ instead of quotation marks (").

*Some examples :*  

The examples given below are given with grep because it is the simplest tool. If you use more advanced tools, such as SED, be careful with the metacharacter protection (to be escaped with "\" if necessary).

````sh
# filter the lines that contain a string that starts with "ab" and that are followed by a character
grep ab. file.txt

# show commented lines of a BASH script
grep ^# script.sh

# show lines that start with a lowercase letter
grep ^[a-z] file.txt

# search for grey or gray in a string
echo grey |grep -E "gr(a|e)y"
  # is equivalent to
echo grey |grep gr[ae]y

echo graaaaaaaaaaaaaaaaaaaaaaay |grep -E "gra+"
echo grabababaaaaaaaaaaaaaaay |grep -E "^gr(ae|ab)+.*y$"
````

### Filtering with grep
Grep is one of the most used command line tools. It allows you to display, among the lines you give it as input, only the lines corresponding to certain criteria.

It is largely thanks to grep that we can interact with a terminal without having to read a huge amount of text. Filtering is mostly used to focus only on the content that interests us.

Grep accepts files as parameters or can also read from standard input. The mandatory parameter is the filter pattern.

> ⚠️ grep does not filter on lines that exactly match the pattern passed in parameter. Grep looks for the presence of the pattern inside each line.

- Simple use of grep:
    ````sh
    # displays the lines of file.txt that contain "plop"
    grep "plop" file.txt
    # is equivalent to 
    cat file.txt | grep "plop"
    ````
- Start and end of line:
    ````sh
    # lines that start with "hello
    grep "^hello" file.txt
    # lines that end with "goodbye
    grep "aurevoir$" file.txt
    ````

- More complex examples:
    ````sh
    # lines that contain "hello" and "goodbye
    grep "goodbye" file.txt | grep "hello

    # lines that contain letters, spaces or commas in parentheses
    grep "([a-z ,]*)" file.txt
    ````

- You can also use grep in extended mode to use more complex regular expressions. Just add the "-E" option or directly "egrep" instead of "grep".
    ````sh
    # does not display commented and empty lines
    egrep -v "^#|^$" file.txt
    ````

In the above example, we do not display comments (comments often start with '#' in configuration files) or empty lines (combination of reverse search with "-v" option and insertion of "logical OR" with the use of "|" symbol).

If you are used to regular expressions in PERL, you can also use them by adding the "-P" option to grep.

Some other useful options to grep: "-r" (recursive), "-i" (insensitive case), "-AN" where N is a number (N After: displays N line after), "-BN" (same as above but N Before)


## Various tools (cut, sort, wc, uniq, diff)

There are a lot of command line text analysis tools. Here is a non-exhaustive list:

### cut
The main function of the tool cut is to isolate a column for all the lines of the input content.

If you have a file of type :

````
val1A,val1B,val1C
val2A,val2B,val2C
val3A,val3B,val3C
````
and we want to obtain the following result: 
````sh
val1B
val2B
val3B
````

we must type the following command:

````sh
cut -d "," -f 2 file.txt
````

The option "-d" allows to define the column delimiter. The option "-f" allows to define which column we want to select.

### uniq
uniq deletes the consecutive identical lines. Note that uniq does not delete lines that appear several times if they are not consecutive. The sort tool, presented next, is therefore often complementary to uniq.
````sh
# or the following file:
$ cat file.txt
one
two
three
three
two
four
four
````
Here is the result of uniq :

````sh
$ cat file.txt | uniq
one
two
three
two
four
````

### sort
As its name suggests, sort is used to sort rows.

It has a "-u" option which will apply the "uniq" command to the result of sort. In this way, duplicate rows are removed even if they are not consecutives.

````
sort file1 file2 | uniq
````

### wc
wc is an extremely useful command that counts the number of characters, words or lines in a text.

example: how many lines (without duplicates) a file has:
````sh
sort -u file.txt | wc -l
````
how many lines start with the letter "a" :
````sh
grep "^a" file.txt | wc -l
````

Other counting tools can also be useful: bc, nl (respectively command line calculator and a tool for counting lines in a file).

### diff
diff is a tool to compare files line by line. It allows to see in a synthetic and precise way the differences between two files.

It is widely used in software development to facilitate collaboration between programmers.

syntax :

````sh
diff file1.txt file2.txt
````

diff also allows to compare directories with the "-r" option

See also the sdiff command !

### sed 
Sed is a VERY versatile non-interactive word processing tool. As the title of its man page says:

"sed is a stream editor for filtering or transforming text."

It is an ultra powerful and efficient tool to do line by line processing on text content. We will talk here about the main features of sed: pattern replacement, insertion and filters.

Some external documentation links:

* http://www.shellunix.com/sed.html
* http://okki666.free.fr/docmaster/articles/linux130.html
* http://www.grymoire.com/Unix/Sed.html
* http://fr.openclassrooms.com/informatique/cours/la-commande-sed

sed accepts one or more input files as parameters but also and especially a standard input stream. So we can pass content to sed by a PIPE :

````
program_verbose | sed ...
````

By far the most common use of sed is pattern matching, which can be thought of as the "find/replace" function in conventional text editors like OpenOffice.

The syntax is as follows:
````sh
$ sed 's/PATTERN/REPLACE/OPTIONS' file.txt
````

When you apply a sed replacement to a file, it is not modified by default. Sed will display the contents of the file by applying the replacement. If you want the changes to be applied directly to the file you must use the -i option of sed. For complex replacements using extended regular expressions, we will add the "-r" option to sed.

> ⚠️ WARNING by default sed replaces only the first occurrence of the pattern in each line. To replace all occurrences in each line, you must specify the g option. For example :

````sh
echo "aa bb aa" | sed 's#aa#zz#'
# the result is: "zz bb aa"

# whereas if we add the option g :
echo "aa bb aa" | sed 's|aa|zz|g'
# we get "zz bb zz"
# if we want to change only the 2nd occurrence of aa

echo "aa bb aa" | sed 's/aa/zz/2'
# with the parenthesis, we can keep in memory a pattern if it has been found and use it in the right part of the 
# substitution
# in this example the letter sequence is represented by \1

echo abcd123 | sed 's/\([a-z]*\).*/\1/'
# here we reverse the sequence of letters and the sequence of numbers
# we have two parenthesized blocks, the first of letters and the second of numbers

echo abcd123 | sed 's/\([a-z]*\)\([0-9]*\)/\2\1/'
echo abcd123 | sed -r 's/([a-z]*)([0-9]*)/\2\1/'
# the result is "123abcd"
````

Lines containing the specified pattern can be deleted with the sed command "d":
````sh
sed '/pattern/d' file.txt
````

Deleting a particular line (here line 25)
````sh
sed '25d' file.txt
````

Deletion of a range of lines (here from 3 to 25)
````sh
sed '3,25d' file.txt
````

Delete line 1 and every 2 lines after (odd lines)
````sh
sed '1~2d' file.txt
````

Delete empty lines:
````sh
sed '/^$/d' file.txt
````

To apply the deletion directly to the file, we use the -i option:
````sh
sed -i '/motif/d' file.txt
````

To keep a copy of the original, we add the name of the extension behind the -i option:
````sh
sed -i.bak '/pattern/d' file.txt
````

### awk

Awk is a scripting language used for manipulating data and generating reports. The awk command programming language requires no compiling and allows the user to use variables, numeric functions, string functions, and logical operators. 

Awk is a utility that enables a programmer to write tiny but effective programs in the form of statements that define text patterns that are to be searched for in each line of a document and the action that is to be taken when a match is found within a line. Awk is mostly used for pattern scanning and processing. It searches one or more files to see if they contain lines that matches with the specified patterns and then perform the associated actions.

**Example:*** 

Consider the following text file as the input file for all cases below: 

````sh
$ cat > employee.txt 
# output
ajay manager account 45000
sunil clerk account 25000
varun manager sales 50000
amit manager account 47000
tarun peon sales 15000
deepak clerk sales 23000
sunil peon sales 13000
satvik director purchase 80000 
````
#### By default Awk prints every line of data from the specified file. 

````sh
$ awk '{print}' employee.txt
# output
ajay manager account 45000
sunil clerk account 25000
varun manager sales 50000
amit manager account 47000
tarun peon sales 15000
deepak clerk sales 23000
sunil peon sales 13000
satvik director purchase 80000
````

In the above example, no pattern is given. So the actions are applicable to all the lines. Action print without any argument prints the whole line by default, so it prints all the lines of the file without failure.

#### Print the lines which match the given pattern. 

````sh
$ awk '/manager/ {print}' employee.txt 
# output
ajay manager account 45000
varun manager sales 50000
amit manager account 47000 
````
In the above example, the awk command prints all the line which matches with the ‘manager’.

#### Splitting a Line Into Fields

For each record i.e line, the awk command splits the record delimited by whitespace character by default and stores it in the $n variables. If the line has 4 words, it will be stored in $1, $2, $3 and $4 respectively. Also, $0 represents the whole line.

````sh
$ awk '{print $1,$4}' employee.txt 
# output
ajay 45000
sunil 25000
varun 50000
amit 47000
tarun 15000
deepak 23000
sunil 13000
satvik 80000 
````

## Exercises 

1. Search all sequences containing "Loxondota" in ``/home/student/lorem.txt``
    > Flag : BC{GREP_ME_LOREM_FL4G}
2. Copy the file /etc/passwd to your home directory. Display the line starting with ``student`` name.
    > Your commands : sudo cp /etc/passwd /home/ - grep ^"student" passwd
3. Display the lines in the passwd file starting with login names of 3 or 4 characters.
    > Your commands : egrep '^[^:]{3,4}:' passwd
4. In the file ``/home/student/sample.txt`` how many different values are there in the first column? in the second?
    > Your response :  4/4
    > Your command : cut -d "," -f 1 sample.txt | sort | uniq | wc -l/cut -d "," -f 2 sample.txt | sort | uniq | wc -l
5. In the file ``/home/student/sample.txt`` sort the values in the second column by frequency of occurrence. (uniq -c can be useful)
    > Your response :  1 11/1 30/2 10/ 4 20 
    > Your command : cut -d "," -f 2 sample.txt | sort | uniq -c | sort
6. In the file ``/home/student/iris.data`` Change the column separator (comma) to tab (make sure that the changes are applied to the file)
    > Your response :  
    > Your command : sudo sed -i 's|,|\t|g' iris.data
7. In the file ``/home/student/iris.data``, extract from this file the column 3 (petal length in cm) (use cut )
    > Your response :  
    > Your command : cut -f 3 iris.data
8. In the file ``/home/student/iris.data``, count the number of flower species (cut and uniq)
    > Your response :  
    > Your command : cut -f 5 iris.data | grep -v '^$' | sort | uniq | wc -l
9. In the file ``/home/student/iris.data``, sort by increasing petal length (see sort options)
    > Your response :  
    > Your command : sort --field-separator=$'\t' --key=3n  iris.data
10. In the file ``/home/student/iris.data``, show only lines with petal length greater than the average size
    > Your response :  
    > Your command : awk -F"\t" '
{
    if ($3 != "") {
        sum += $3; n++; righe[NR] = $0; valori[NR] = $3
    }
}
END {
    if (n > 0) {
        media = sum / n
        for (i = 1; i <= NR; i++)
            if (valori[i] > media)
                print righe[i]
    } else
        print "Nessun valore valido"
}
' iris.data
11. Using ``/etc/passwd``, extract the user and home directory fields for all users on your student
machine for which the shell is set to ``/bin/false``. 
    > Your response :
    > Your command awk -F: '$7 == "/bin/false" {print $1, $6}' /etc/passwd


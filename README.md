# command Line Interface (CLI) With Golang



Welcome to this advanced guided project on using go
language to connect to a cloud provider. By the end
of this project
you will have built a command line interface using the go
programming language.
This project is for any programmer who is looking to advance
their software development career by learning go.
In order to be successful in this project, you will need
to know some basic constructs of programming as well as have
a simple working knowledge of the Windows Operating System.
My name is Meghna and I will be your instructor.
As a technical educator for over 22 years
I have designed training programs around various programming
languages including go.
Now let's get started with our project. For the purpose
of this project
imagine you are a system engineer trainee working
at Infosys. One of the major responsibilities in this role
is implementing software solutions required by the company.
You have been assigned the responsibility to build a command
line interface that can help Infosys employees in connecting
to the private cloud available at Infosys using Go language.
The first step in getting towards this goal of building
a command line interface in go is to test the golang
installation in your project environment.
It has already been installed for you as a part
of the workspace set up.
You will open the command prompt by clicking the shortcut
provided on your desktop and execute the command "go version".
  
Confirm that the command prints the installed
version 1.17 of go on your screen.
Great. You have just completed the Golang installation in your
project environment.
  
Let us see the command line interface you will build in
this guided project.
The command line prompt will accept commands from the end
user. The commands you will support are exit
and checkinfyconnect. exit will terminate the command line
interface and exit the program. checkinfyconnect will
execute the ping command in the background to test
connectivity with any machine on the cloud.
Let us see these commands in action.
  
 For checkinfyconnect command
I am using the IP address of the VM assigned to me.
The exit command terminates the command line interface.
A code template with steps to implement
this program is shared as CLIUsingGolang.go file in the
CLIUsingGolang folder on your desktop.
Let us go through the code template.
The documentation for each step is provided as comments
which include a toolkit for you.
The toolkit specifies input for each step, variable names
used, functions to be used, packages that the functions belong
to, and output if any.
In some cases it also includes the struct that the function
belongs to within a package.
You need to build the program by adding code after the
comment for the step. You will need to pay careful attention
to the scope of the program statements
you write like looping constructs or method boundaries. In the
next task
you will complete the step one of the code template to
create the prompt for the command line interface.




Welcome back. In the last task we verified the golang
installation.
You are now ready to code your program in golang.
You will start by creating the initial display
with the prompt for the command line interface
we aim to build in this guided project.
Use the code template shared in the using CLIUsingGolang folder on your
desktop.
Throughout this project you will be completing the steps
in the code template shared with you.
This is so that we can make the most out of the short time
we have. Let's open this program together. On your desktop,
navigate to the folder CLIUsingGolang. Right click to open
the CLIUsingGolang.go file
using sublime text editor.
  
Here you see a comment "Step 1" with the instructions
to complete the first step in building your program.
This program starts with a package declaration.
Go programs are organized into packages.
A package is a collection of source files in the same
directory that are compiled together.
The main package is a special package which is used
with the programs that are executable
and this package contains the main function.
The main function is the entry point of the executable
program.
It does not take any argument nor returns anything. Go
automatically
Calls the main function So there is no need to call the main
function explicitly.
Every executable program must contain a single package
with the main function. import statement is used to import the
packages required for this program.
Used to Println function of the fmt package
to display the prompt for the CLI. Pause the video and
complete this on your own.
When we return to the task, we will go over the solution
together.
Welcome back!
The solution for "Step 1" is shared on your screen. Comment out
the imports not required for this program execution.
This activity needs to be done for all the tasks we will work
on henceforth. You will also need to provide a return
statement for the execPINGCommand function.
The string value returned by
this function will be the name of the function.
This function will be implemented in a later task.
Run the code using the "go run CLIUsingGolang.go" command.
 
  
You can see the prompt for our CLI printed on the
console.
Wonderful.
You are now ready to take on the next challenge to create a
command line interface using Go.




Welcome back. In the last task we built and executed
the program to display the CLI prompt to the end user.
By the end of this task you will be able to create a command
line interface using go.
Now let's get started. Ensure that the CLIUsingGolang.go
file placed in the folder
CLIUsingGolang on your desktop is open. In Step 2
you will add an infinite for loop that accepts input
from the end user.
This will enable the CLI to accept a command from the end
user, echo the command and wait at the prompt
for another command to be input. To do this,
you will use a scanner created using the new scanner function
of the bufio package. This function accepts os.Stdin
object as a parameter.
Bufio implements buffered I/O and can be used for textual
input and output.
The package os provides a platform independent interface
to the operating system functionality. Stdin, Stdout
and standard error
are open files pointing to the standard input, standard output
and standard error file descriptors.
An infinite for loop will accept a string input
from the console
using the Scan function, which advances the scanner
to the next input token.
The Scan function returns true when a valid input token is
available and false when the scan stops either by reaching
the end of the input or an error.
The input token received through the Scan function
can be retrieved as a string using the Text method.
Pause the video here and complete this step.




We will see the solution once you restart this video.
Welcome back.
Let's look at the solution together.
The NewScanner function returns a reference to the
scanner object in a variable named scanner. go is a strongly
typed language but it offers implicitly and explicitly typed
variables.
Here scanner is an implicitly typed variable.
Inside functions the colon equal to := short assignment  
statement can be used in place of a var declaration
with the type specified explicitly.
You can see that userInput variable name uses MixedCaps.
The convention in go is to use MixedCaps rather than
underscores to write multi-word names.
If an identifer needs to be visible outside the package,
its first character should be uppercase if you don't have the
intention to use it in another package, you can safely stick
to MixedCaps.
The infinite for loop used here accepts a string input from
the console using the Scan function which advances the
scanner to the next input token.
os.Stdin is an open file pointing to the
standard input file descriptor.
The Scan function of the scanner returns true when a valid
input token is available and false when the scan stops either
by reaching the end of the input or an error.
The input token received through the Scan function can be
retrieved as a string using the Text method in the variable
userInput.
Run the code using the "go run CLIUsingGolang.go"
command.
The program displays a prompt and waits for user input.
It echoes the input received, and then displays the prompt
again to receive more input from the user.
You are now ready to take on the next challenge to
implement an exit command to quit the command line interface
and terminate the program.





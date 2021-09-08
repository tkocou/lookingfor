# lookingfor
Python-3 script to search a directory of source code files looking for a specified text

For everyone running Linux, the '.py' extension can be removed after the permissions have been fixed to allow execution. (lookingfor.py becomes lookingfor)

lookingfor - this program was created out of the need to find which file had the text that I was looking for. I had the source for a project, but the source code was spread over many dozens of .cpp files and finding which file had the text was comparable to looking for a needle in a hay stack.
I tried using grep. However, while the contents were shown, there was no indication of which file was being displayed.

lookingfor is a CLI script and needs to be ran in a terminal window. Copy 'lookingfor' into a suitable directory which is referenced like $USER/bin ( a bin directory in your home directory)

Use examples:

            V----Two single quotes - back to back to indicate a blank option
            V
lookingfor '' base  :This configuration will search by known extensions and search the contents of each targeted file for 'base' in the current directory

lookingfor .h   :This configuration will use '.h' as the file extension and search the contents of each targeted file for the default of 'def' in the current directory

Let's say that you are in the base directory of a project and the source code files are held in the directory 'src'.

lookingfor '' struct ./src  :This configuration will search by known extensions and search the contents of each targeted file for 'struct' in the './src' directory

Let's say that you are in the base directory of a Python project and the source code scripts are stored in 'source'.

lookingfor .py connect ./source  :This configuration will use '.py' as the file extension and search the contents of each targeted file for 'connect' in the './source' directory

Absolute paths work just as well as relative paths. So you need to search in a directory completely different from the one which you are currently at, use the absolute path to the target directory.

Another use for 'lookingfor' would be a situation where you are reading a source code file and it references a "function()" which is not in that file. You can tell 'lookingfor' which "function()" to search for in the same directory where you are at.

Example:
lookingfor '' readMessage( 

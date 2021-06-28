# Xampp_Python :computer: :snake:
## In this project, I would develop a HTTP Web Server (XAMPP) by Python instead of PHP as usual 
### **Convenience:**
1. By using this format, we can take advantage of Python for data/variable processing
1. And it is friendlier to ones who is familiar with Python (compare with Javascript or PHP)
### **Inconvenience:**
* When creating this project, I feel that XAMPP haven't support as many feature for Python as I has expected (such as Numpy, Pandas,...)  
### **To implement this project, we have to do steps in following order:**
1. Setup XAMPP Server:
   * Download from this [download link](https://www.apachefriends.org/index.html)
   * Run file setup (or follow [Setup XAMPP Guide for Windows](https://github.com/philongvn99/Xampp_Python/blob/master/How%20to%20Install%20XAMPP%20on%20Windows.pdf)
   * Configure XAMPP for Python:
       * *Optionally*, you can change folder of root source code by replacing DocumentRoot in /xampp/apache/conf/httpd.conf by address of your desired folder
       * Find *AddHandler* in **above file** and add *.py* to that line; besides, add *ScriptInterpreterSource Registry-Strict* below that line if it haven't existed  
       ```
       AddHandler cgi-script .py  
       ScriptInterpreterSource Registry-Strict
       ```
       * Find **IfModule dir_module** in *above file* and add *index.py* to that line;  
       ```
       <IfModule dir_module>  
        DirectoryIndex index.php index.pl index.cgi index.asp index.shtml index.html index.htm  
        default.php default.pl default.cgi default.asp default.shtml default.html default.htm  
        home.php home.pl home.cgi home.asp home.shtml home.html home.htm index.py  
       </IfModule>
       ```
   * Restart XAMPP to apply changes
1. Modify python file
   * In each python file, you should add `#! <python.exe link on your system>` at very the first line
   * For exchange data between Python and HTML file, *cgi* library is recommended to be used because its simplicity and perspicuity. For more knowledge, you could visit this [G4G link of CGI](https://www.geeksforgeeks.org/what-is-cgi-in-python/)    
### Hope you enjoy and contribute to help developing this method. 
### Please give me some feedbacks if you have any opinion about this projects.
### Thank you very much! :two_hearts:

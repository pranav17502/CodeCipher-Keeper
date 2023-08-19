
# CodeCipher Keeper

CodeCipher Keeper is a powerful password manager designed for top-tier security and user-friendly access. It utilizes hashing technology to store your passwords securely. With a "copy to clipboard" feature, your passwords are readily available without compromising security. This works on command line. 

Ensure your digital security with CodeCipher Keeper today.


## Features

- Developed a robust Python-based password manager with MySQL integration, designed to securely store and manage sensitive online credentials
- Implemented advanced hashing techniques to protect user passwords, ensuring that they remain highly secure even in the event of a breach.
- Utilized the AES encryption algorithm to safeguard stored passwords, allowing only authorized users to access the data.
- Designed an intuitive command-line interface (CLI) for user interaction, enhancing user-friendliness and ease of use.
- Incorporated the capability to generate and store device-specific secrets, enhancing the security of the stored data while providing a personalized experience.
- Created a database configuration module for seamless interaction with MySQL, ensuring efficient and reliable data storage and retrieval.
- Enabled users to add, search, and retrieve entries using a variety of parameters such as site name, site URL, email, and username.
- Integrated the Rich library to present search results in a visually appealing tabular format, enhancing the readability of retrieved data.
- Implemented a secure copying feature using the Pyperclip library, enabling users to copy decrypted passwords to the clipboard while maintaining data confidentiality.
- Utilized Crypto libraries for key derivation and AES encryption, ensuring strong cryptographic practices and data security.
- Demonstrated proficiency in Python, MySQL, cryptography, and database management, showcasing the ability to create a robust and secure software solution.
- Designed the project with a focus on security, convenience, and user experience, providing users with a reliable and efficient tool for managing their online credentials.
- Collaborated with colleagues to review and improve the codebase, enhancing the quality and security of the project through code reviews and continuous improvements.
- Engaged in testing and debugging to identify and resolve issues, ensuring the stability and reliability of the password manager application.



## Clone the project

```bash
  git clone https://github.com/pranav17502/CodeCipher-Keeper/
```
## Cofigure
Run on command line.
To configure and set a master password.

```bash
    python configure.py
```
This would have to run only once. This is for creating table in MySQL and configuring. If this is ran again, it will give error that the database has already been created. 

## Adding new entry
```bash
    python pm.py add -s <sitename> -u <siteurl.com> -e <youremail.com> -l <yourLoginId>
```
After this program will ask for master password. Enter the master password you have set. Then the program would ask for the password of the about entry. Write the password and hit enter. The entry would get added in the database

## Extracting the field
To see all the entries
```bash
    python pm.py e
```
This will show all the entries in the database in a tabular format. 

To extract a particular entry, use a search field. The format for searching a particular entry is:
```bash
    python pm.py e -<l> <yourFieldName>
```

## Copying the password to Clipboard
The program does not directly show the password on CMD. The only way to use the password is that the program directly copies the password to the clipboard. To do so, we have to use the above extract command and add -c at the end.

```bash
    python pm.py e -<l> <yourFieldName> -c
```




## Usage/Examples
For searching based on Site Name
```bash
    python pm.py e -s facebook 
```
For searching based on Site URL
```bash
    python pm.py e -u facebook.com 
```
For searching based on emailID
```bash
    python pm.py e -e youremailID.com 
```
For searching based on loginID
```bash
    python pm.py e -l yourLoginID 
```
For copying
```bash
    python pm.py e -s facebook -c
```
## 🛠 Skills
Cryptography, python, MySQL Database, hashing, Encryption-Decryption, Command line interface development, rich library, pyperclip library, cryptographic library, Information Privacy

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://pranav17502.github.io/BinaryOdyssey.github.io/)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/pranavchaudhariiitbombay)

[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/pranav17502)


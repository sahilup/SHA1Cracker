import hashlib
def sha1_converter(pas):    #To convert the simple text into SHA1 code
    passwd_sha1 = hashlib.sha1(pas.encode()).hexdigest()
    return passwd_sha1
def main():
    sha1_code_input = input("Enter the SHA1 code:")
    clean_sha1_code = sha1_code_input.strip().lower()
    dictionary_list = input("Enter the full location of the password dictionary:")
    with open(f'{dictionary_list}') as p:
        for psw_lines in p: #looping within the user given dictionary
            password = psw_lines.strip()
            password_to_sha1 = sha1_converter(password) #comparing user given hash with converted hash
            if clean_sha1_code == password_to_sha1:
                print(f"The password is as following: {password} \n")
                return 
    print("Could not find the password")
    
if __name__ == "__main__":
    main()

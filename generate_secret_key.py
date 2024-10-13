import os

def generate_secret_key():
    secret_key = os.urandom(24).hex()
    print(f"Generated SECRET_KEY: {secret_key}")
    
    # Optionally, write to .env file
    with open(".env", "a") as env_file:
        env_file.write(f"\nSECRET_KEY={secret_key}\n")
    
    print("SECRET_KEY added to .env file.")

if __name__ == "__main__":
    generate_secret_key()

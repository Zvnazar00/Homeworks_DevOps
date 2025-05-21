import os
import subprocess

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
PROJECT_DIR = "/home/vagrant/spring-petclinic"

subprocess.run("sudo apt-get install -y openjdk-11-jdk git", shell=True, check=True)

if not os.path.exists(PROJECT_DIR):
    subprocess.run(f"git clone https://gitlab.com/zvenyhorodskyi.nazar/step_project_1.git {PROJECT_DIR}", shell=True, check=True)

subprocess.run(f"chmod +x {PROJECT_DIR}/mvnw", shell=True, check=True)

subprocess.run(f"cd {PROJECT_DIR} && ./mvnw package", shell=True, check=True)


bashrc = "/home/vagrant/.bashrc"
with open(bashrc, 'a') as f:
    f.write(f"\nexport DB_HOST={DB_HOST}")
    f.write(f"\nexport DB_PORT={DB_PORT}")
    f.write(f"\nexport DB_NAME={DB_NAME}")
    f.write(f"\nexport DB_USER={DB_USER}")
    f.write(f"\nexport DB_PASS={DB_PASS}")

target_dir = os.path.join(PROJECT_DIR, 'target')
if os.path.exists(target_dir):
    jars = [f for f in os.listdir(target_dir) if f.endswith(".jar")]
    if jars:
        jar_path = os.path.join(target_dir, jars[0])
        subprocess.Popen(f"nohup java -jar {jar_path} &", shell=True)

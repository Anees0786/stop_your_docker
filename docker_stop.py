

import subprocess

def stop_all_containers():
    try:
        subprocess.check_output(
            ["sudo", "docker", "kill", "$(docker ps -a -q)"],
            stderr=subprocess.STDOUT,
            text=True,
        )
        docker_ps = subprocess.check_output(
            ["sudo", "docker", "ps"],
            stderr=subprocess.STDOUT,
            text=True,
        )
        return "All Docker containers stopped successfully.", docker_ps
    except subprocess.CalledProcessError as e:
        return f"Error: {e}", ""

def main():
    output, docker_ps = stop_all_containers()
    
    print("Output:")
    print(output)
    print("Docker PS:")
    print(docker_ps)

if __name__ == "__main__":
    main()

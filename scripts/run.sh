sudo docker build -t prep ./preprocessing/.
echo "--------------- Starting container -----------------"
sudo docker run -v "$PWD"/preprocessing/data:/script_data prep

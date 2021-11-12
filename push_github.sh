#cd /home/cuongtv/strapi/
git add -A
git commit -a -m "daniel"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/strapi_ssh
git push origin HEAD:main
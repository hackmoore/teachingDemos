# Webserver files
This folder contains files that are intended to be placed in the `/var/www/html` folder of a NGINX/php-fpm server running on a VM.

You can replicate this setup by performing the following steps:
1. Install Hypervisor (such as virtuabox)
2. Install ubuntu desktop
3. Follow this tutorial to setup Nginx and php-fpm https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/Nginx-PHP-FPM-config-example
4. Download the files in this repository to the appropriate folder (listed above)
5. Test the server on your local machine by visiting http://localhost
6. Get your IP address by running `ip addr` in the terminal and looking for your ip address (or use the GUI to obtain)
7. Access the page using your host OS via the obtained IP Address
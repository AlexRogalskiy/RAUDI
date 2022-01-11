# nikto

## Official Documentation
Reference: https://github.com/sullo/nikto/wiki

## Description
**Nikto** is an Open Source (GPL) web server scanner which performs comprehensive tests against web servers for multiple items, including over 6700 potentially dangerous files/programs, checks for outdated versions of over 1250 servers, and version specific problems on over 270 servers. It also checks for server configuration items such as the presence of multiple index files, HTTP server options, and will attempt to identify installed web servers and software. Scan items and plugins are frequently updated and can be automatically updated.

Nikto is not designed as a stealthy tool. It will test a web server in the quickest time possible, and is obvious in log files or to an IPS/IDS. However, there is support for LibWhisker's anti-IDS methods in case you want to give it a try (or test your IDS system).

Not every check is a security problem. There are some items that are "info only" type checks that look for things that may not have a security flaw, but Pentester may not know are present on the server. These items are usually marked appropriately in the information printed. There are also some checks for unknown items which have been seen scanned for in log files.

The goal of the project is to examine a web server to find potential problems and security vulnerabilities, including:

* Server and software misconfigurations
* Default files and programs
* Insecure files and programs
* Outdated servers and programs
* Pointers to lead a human tester to better manual testing

Nikto is built on LibWhisker2 (by Rain Forest Puppy) and can run on any platform which has a Perl environment. It supports SSL, proxies, host authentication, attack encoding and more.

## Usage
```
docker run -it --rm secsi/nikto -h <target_url>
```

## 🐳 RAUDI: Regularly and Automatically Updated Docker Images

Hello, friend. This Docker Image has been created by RAUDI. What is RAUDI?

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

If you want to contribute, give us a star or take a quick look at the source code of **RAUDI** click [here](https://github.com/cybersecsi/RAUDI).
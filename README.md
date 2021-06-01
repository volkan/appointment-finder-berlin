# Berlin Appointment Finder

## Services

1. Go to the services page

    [Service list](https://service.berlin.de/terminvereinbarung/)

        * Apply for ID card
        * Register an apartment
        * Apply for a passport
        * Business registration

    Pick one like [Registration of an apartment](https://service.berlin.de/dienstleistung/120686/)

    Pick office like [District office Friedrichshain - Kreuzberg](https://service.berlin.de/terminvereinbarung/termin/tag.php?termin=1&anliegen[]=120686&dienstleisterlist=122231,122243&herkunft=http%3A%2F%2Fservice.berlin.de%2Fdienstleistung%2F120686%2F) and copy the appointment URL

2. Go to the [pushover service page](https://pushover.net/)
    * Create an account (1 week free)
    * Create an Application/API Token
    * Download mobile app and login.

## How can I use it?

    * Update `TARGET_URL` with office URL in `.env`
    * Update pushover API credentials in `.env`

## Requirements & Setup:
```shell
$ mkdir -p ~/projects/ && cd ~/projects/
$ git clone https://github.com/volkan/appointment-finder-berlin.git
Cloning into 'appointment-finder-berlin'...

$ cd appointment-finder-berlin
$ cp .env.dist .env
$ vi .env # for change, credentials, and URL
$ docker-compose up

```

### Crontab
```shell
* * * * * cd ~/projects/appointment-finder-berlin && /usr/local/bin/docker-compose up
```
# Berlin Appointment Finder

## Services

Go to the services page

[Service list](https://service.berlin.de/terminvereinbarung/)

* Apply for ID card
* Register an apartment
* Apply for a passport
* Business registration

Pick one like [Registration of an apartment](https://service.berlin.de/dienstleistung/120686/)

Pick office like [District office Friedrichshain - Kreuzberg](https://service.berlin.de/terminvereinbarung/termin/tag.php?termin=1&anliegen[]=120686&dienstleisterlist=122231,122243&herkunft=http%3A%2F%2Fservice.berlin.de%2Fdienstleistung%2F120686%2F) and copy the appointment URL


## How can I use:

    * Update `target_url` with office URL in `myspider.py`
    * Update [https://pushover.net/](https://pushover.net/) API credentials (1 week free) in `myspider.py`

## Requirements & Setup:
```shell
$ git clone https://github.com/volkan/appointment-finder-berlin.git
Cloning into 'appointment-finder-berlin'...

$ cd appointment-finder-berlin/docker
$ docker-compose up

```
#!/bin/bash

function print_help {
echo -e """
USAGE:\n    $0 [ -sd ] [ -h ]
\t-r: Re-build Docker containers.
\t-h: Print this help text.
"""
    exit 0
}

function clean_app_instance {
    echo '[*] Cleaning up Docker environment!'
    docker-compose down
    fi
}

while getopts ':hdr' ARG; do
    case ${ARG} in
        h)
            print_help
            ;;
        r)
            AUTOSTART_NEW_INSTANCE=true
            ;;
        *)
            print_help
            ;;
    esac
done

if [[ -n ${AUTOSTART_NEW_INSTANCE} ]]; then
    clean_app_instance
elif [[ -n $(docker container ls -a | grep -o 'conduit') ]]; then
    echo '[*] Conduit containers currently exist!'
    read -p '[*] Remove existing Conduit instance? [y/n] ' -r

    while [[ ! ${REPLY} =~ ^[yYnN]$ ]]; do
        read -p "[*] Invalid input. Do you want to remove the existing Conduit instance? [y/n] " -r
    done

    if [[ $REPLY =~ ^[Nn]$ ]]; then
        echo '[*] Containers intact! Stopping initialization...'
        exit 1
    else
        clean_app_instance
    fi
fi

docker compose up --build

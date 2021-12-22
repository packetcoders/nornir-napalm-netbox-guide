if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Nornir Helper CLI")
    parser.add_argument(
        "-i", "--inventory", action="store_true", help="show inventory", required=False
    )
    parser.add_argument(
        "-n", "--netbox", action="store_true", help="netbox debug", required=False
    )

    args = vars(parser.parse_args())
    if args["inventory"]:
        print(__init__.nr.inventory.dict())
    elif args["netbox"]:
        # to be used with python -i
        netbox = NetBox(
            host=__init__.nb_host,
            port=__init__.nb_port,
            use_ssl=False,
            auth_token=__init__.nb_token,
        )

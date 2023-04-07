from src.search import main, parse_args

if __name__ == "__main__":
    args = parse_args()
    main(args.file_path)

def test_output(capsys):
    from hello_world import main
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"

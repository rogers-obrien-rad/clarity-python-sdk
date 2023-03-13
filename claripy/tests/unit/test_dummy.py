class TestDummy:

    def test_str(self):
        """
        Dummy function for str
        """
        text = "Hello World"
        assert isinstance(text,str)

    def test_int(self):
        """
        Dummy function for int
        """
        num = 1
        assert isinstance(num,int)

    def test_list(self):
        """
        Dummy function for list
        """
        li = ["a","b","c"]
        assert isinstance(li,list)
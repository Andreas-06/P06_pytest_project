from calculator.calculator import Calculator


class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 2
        b = 4
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = -2
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 3
        b = 4
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 12
        assert result == expected

        def test_divide(self):

            # Arrange (test for normal division)
            a = 12
            b = 3
            expected = 4
            cal = Calculator()

            # Act (normal division)
            result = cal.divide(a, b)

            # Assert (normal division)
            assert result == expected

            def test_divide(self):

                # Arrange (test for when denomiator is 0) 
                a = 12
                b = 0

                cal = Calculator()

                # act + assert 
                with Calculator.raises(ZeroDivisionError): 
                    cal.divide(a,b)

            

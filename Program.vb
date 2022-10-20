Imports System

Module Program
    Sub Main(args As String())
        Dim Data As String = "38 38 38"
        Console.WriteLine("Hello Wooorld!")
        Dim result As String

        Dim arr1() As String = Data.Split(" "c)
        result = String.Join("", arr1)
        Console.WriteLine(result)
        Console.WriteLine(arr1(0))
        Console.WriteLine(arr1(1))
        Console.WriteLine(arr1(2))
        Debug.Print(result)
        Dim x As Int16 = Convert.ToInt32(arr1(0), 16)
        Console.WriteLine(x)
        Dim bb As Byte = Convert.ToByte(x)
        Console.WriteLine(bb)
        Debug.Print("hello")
        Dim data2() As String = Data.Split(" "c).Select(Function(n) n + "hello").ToArray

        Console.WriteLine(data2(0))
        'Dim c As CRC.Crc = New CRC.Crc(CRC.CrcStdParams.StandartParameters(CRC.CrcAlgorithms.Crc16X25))
        Dim str2 As String = "hello"
        '2 len, 0 index
        Console.WriteLine(str2.Substring(0, 2))


        Dim bytes As Byte() = Data.Split(" "c).Select(Function(n) Convert.ToByte(Convert.ToInt32(n, 16))).ToArray()
    End Sub
End Module

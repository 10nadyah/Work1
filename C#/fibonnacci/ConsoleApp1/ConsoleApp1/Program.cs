using System;
using System.Threading;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Value:");
            string fibValue = Console.ReadLine();
            int fibNumber;
            Int32.TryParse(fibValue, out fibNumber);
            int counterValue = 0;
                int fib1 = 0;
                int fib2 = 1;
            Convert.ToInt32(fibValue);
            int sleep = 500;

            if (fibNumber > 100)
            {
                sleep = 100;
            }
            if (fibNumber > 1000)
            {
                sleep = 50;
            }
            if (fibNumber > 10000)
            {
                sleep = 1;
            }

            while (fibNumber > counterValue)
            {
                
                Console.Write(fib1 + " , ");
                int fib3 = fib1 + fib2;
                fib1 = fib2;
                fib2 = fib3;
                counterValue = counterValue + 1;
                Thread.Sleep(sleep);
                
            }
            Console.WriteLine("Program Finished");
            Thread.Sleep(10000);
        }
    }
}

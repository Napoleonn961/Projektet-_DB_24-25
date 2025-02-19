using System;

namespace SistemiINotave
{
    class Program
    {
        static void Main(string[] args)
        {
            string vazhdo;
            do
            {
                Console.WriteLine("Mirësevini në Sistemin e Notave!");

                Console.Write("Shkruani pikët për detyrat: ");
                decimal pikeDetyra = Convert.ToDecimal(Console.ReadLine());

                Console.Write("Shkruani pikët për kuizet: ");
                decimal pikeKuize = Convert.ToDecimal(Console.ReadLine());

                Console.Write("Shkruani pikët për provimin: ");
                decimal pikeProvimi = Convert.ToDecimal(Console.ReadLine());

                decimal notaMesatare = (pikeDetyra + pikeKuize + pikeProvimi) / 3;
                Console.WriteLine("\nLlogaritja...");

                Console.WriteLine($"Nota mesatare: {notaMesatare:F2}");

                char nota;
                switch (notaMesatare)
                {
                    case >= 90 and <= 100:
                        nota = 'A';
                        break;
                    case >= 80 and < 90:
                        nota = 'B';
                        break;
                    case >= 70 and < 80:
                        nota = 'C';
                        break;
                    case >= 60 and < 70:
                        nota = 'D';
                        break;
                    default:
                        nota = 'F';
                        break;
                }
                Console.WriteLine($"Nota: {nota}");

                const decimal pragKalimi = 60;
                if (notaMesatare >= pragKalimi)
                {
                    Console.WriteLine("Urime! Ju keni kaluar kursin.");
                }
                else
                {
                    Console.WriteLine("Fatkeqësisht, ju nuk e kaluat kursin.");
                }

                Console.Write("\nDëshironi të llogarisni notën për një student tjetër? (po/jo): ");
                vazhdo = Console.ReadLine().ToLower();
                Console.WriteLine();

            } while (vazhdo == "po");

            Console.WriteLine("Faleminderit që përdorët Sistemin e Notave!");
        }
    }
}

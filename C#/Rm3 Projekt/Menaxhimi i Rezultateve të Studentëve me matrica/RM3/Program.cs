using System;

namespace App
{
    class Program
    {
        static void Main(string[] args)
        {
            const int numStudents = 5;
            const int numSubjects = 3;
            int[,] scores = new int[numStudents, numSubjects];

            Console.WriteLine("Mirësevini në Menaxhimin e Rezultateve të Studentëve!");
            Console.WriteLine("Fusni noten për secilin student dhe secilën lëndë:");


            for (int i = 0; i < numStudents; i++)
            {
                for (int j = 0; j < numSubjects; j++)
                {
                    Console.Write($"Studenti {i + 1}, Lenda {j + 1}: ");
                    scores[i, j] = int.Parse(Console.ReadLine());
                }
            }

            Console.WriteLine("\nMatrica Fillestare e Rezultateve:");
            PrintMatrix(scores);


            CalculateStudentSumAndAverage(scores);


            Console.Write("\nVendos noten qe doni te kerkoni: ");
            int targetScore = int.Parse(Console.ReadLine());
            SearchScore(scores, targetScore);


            Console.Write("\nVendos koeficentin per te zhumzuar matricen: ");
            double coefficient = double.Parse(Console.ReadLine());
            int[,] multipliedMatrix = MultiplyMatrix(scores, coefficient);
            Console.WriteLine("\nMatrix e re:");
            PrintMatrix(multipliedMatrix);

            FindMaxMinScores(scores);
        }

        static void PrintMatrix(int[,] matrix)
        {
            int rows = matrix.GetLength(0);
            int cols = matrix.GetLength(1);
            for (int i = 0; i < rows; i++)
            {
                for (int j = 0; j < cols; j++)
                {
                    Console.Write(matrix[i, j] + "\t");
                }
                Console.WriteLine();
            }
        }

        static void CalculateStudentSumAndAverage(int[,] scores)
        {
            for (int i = 0; i < scores.GetLength(0); i++)
            {
                int sum = 0;
                for (int j = 0; j < scores.GetLength(1); j++)
                {
                    sum += scores[i, j];
                }
                double average = (double)sum / scores.GetLength(1);
                Console.WriteLine($"Studenti {i + 1} - Shuma: {sum}, mesatarja: {average:F2}");
            }
        }

        static void SearchScore(int[,] scores, int targetScore)
        {
            bool found = false;
            for (int i = 0; i < scores.GetLength(0); i++)
            {
                for (int j = 0; j < scores.GetLength(1); j++)
                {
                    if (scores[i, j] == targetScore)
                    {
                        Console.WriteLine($"Nota {targetScore} e gjetur per studentin {i + 1}, Lenda {j + 1}");
                        found = true;
                    }
                }
            }
            if (!found)
            {
                Console.WriteLine($"Nota {targetScore} nuk ekziston.");
            }
        }

        static int[,] MultiplyMatrix(int[,] scores, double coefficient)
        {
            int[,] result = new int[scores.GetLength(0), scores.GetLength(1)];
            for (int i = 0; i < scores.GetLength(0); i++)
            {
                for (int j = 0; j < scores.GetLength(1); j++)
                {
                    result[i, j] = (int)(scores[i, j] * coefficient);
                }
            }
            return result;
        }

        static void FindMaxMinScores(int[,] scores)
        {
            for (int i = 0; i < scores.GetLength(0); i++)
            {
                int maxScore = scores[i, 0];
                int minScore = scores[i, 0];
                for (int j = 1; j < scores.GetLength(1); j++)
                {
                    if (scores[i, j] > maxScore)
                        maxScore = scores[i, j];
                    if (scores[i, j] < minScore)
                        minScore = scores[i, j];
                }
                Console.WriteLine($"Studenti {i + 1} - Nota me e larte: {maxScore}, Nota me e ulet: {minScore}");
            }
        }
    }
}

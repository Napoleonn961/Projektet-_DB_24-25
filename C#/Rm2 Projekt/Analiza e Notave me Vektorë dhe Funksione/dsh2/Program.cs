using System;

class Program
{
    static void Main()
    {
        const int numGrades = 10;
        int[] grades = new int[numGrades];

        Console.WriteLine("Enter grades for 10 students:");
        for (int i = 0; i < numGrades; i++)
        {
            Console.Write($"Enter grade {i + 1}: ");
            grades[i] = int.Parse(Console.ReadLine());
        }

        Console.WriteLine("\nGrades entered:");
        DisplayGrades(grades);

        int maxGrade = FindMaxGrade(grades);
        int minGrade = FindMinGrade(grades);
        double average = CalculateAverage(grades);
        int threshold = 60;
        int countAboveThreshold = CountGradesAboveThreshold(grades, 0, threshold);

        Console.WriteLine($"\nHighest grade: {maxGrade}");
        Console.WriteLine($"Lowest grade: {minGrade}");
        Console.WriteLine($"Average grade: {average:F2}");
        Console.WriteLine($"Number of grades above {threshold}: {countAboveThreshold}");
    }

    static void DisplayGrades(int[] grades)
    {
        int index = 0;
        while (index < grades.Length)
        {
            Console.WriteLine(grades[index]);
            index++;
        }
    }

    static int FindMaxGrade(int[] grades)
    {
        int max = grades[0];
        for (int i = 1; i < grades.Length; i++)
        {
            if (grades[i] > max)
            {
                max = grades[i];
            }
        }
        return max;
    }

    static int FindMinGrade(int[] grades)
    {
        int min = grades[0];
        for (int i = 1; i < grades.Length; i++)
        {
            if (grades[i] < min)
            {
                min = grades[i];
            }
        }
        return min;
    }

    static double CalculateAverage(int[] grades)
    {
        int sum = 0;
        for (int i = 0; i < grades.Length; i++)
        {
            sum += grades[i];
        }
        return (double)sum / grades.Length;
    }

    static int CountGradesAboveThreshold(int[] grades, int index, int threshold)
    {
        if (index == grades.Length)
        {
            return 0;
        }

        int count = (grades[index] > threshold) ? 1 : 0;
        return count + CountGradesAboveThreshold(grades, index + 1, threshold);
    }
}

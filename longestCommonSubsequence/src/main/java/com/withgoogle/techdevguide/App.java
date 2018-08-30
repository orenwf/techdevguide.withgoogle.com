package com.withgoogle.techdevguide;

import java.util.stream.Collectors;
import java.util.stream.Stream;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

/**
 * Finding the word from a set that has the longest common subsequence with a given source text
 *
 */
public class App 
{
	public static void main( String[] args )
	{
		try (	FileReader sourceFile = new FileReader(args[0]); 
				FileReader dictionaryFile = new FileReader(args[1])	) {
			
			Stream<String> sourceText = (new BufferedReader(sourceFile)).lines();
			Stream<String> dictionary = (new BufferedReader(dictionaryFile)).lines();
			
			char[] sourceString = sourceText.collect(Collectors.joining()).toCharArray();
			String longest = "";
			
			for (String word : dictionary.collect(Collectors.toList())) {
				char[] wordArray = word.toCharArray();
				// count of the number of characters in the current word that form a subsequence in the string
				for (int indexInSourceString = 0, matchLen = 0; indexInSourceString < sourceString.length; indexInSourceString++) {
					for (int indexInWordArray = 0; indexInWordArray < wordArray.length; indexInWordArray++) {
						if (wordArray[indexInWordArray] == sourceString[indexInSourceString]) {
							matchLen++;
							indexInSourceString++;
						}
					}
					if (matchLen > longest.length()) longest = word;
				}
			}
			System.out.println("The word with the longest common subsequence is: "+longest+".");
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintStream;
import java.io.OutputStream;
import java.util.List;
import java.util.Properties;

import edu.stanford.nlp.ling.CoreAnnotations;
import edu.stanford.nlp.ling.CoreAnnotations.SentencesAnnotation;
import edu.stanford.nlp.neural.rnn.RNNCoreAnnotations;
import edu.stanford.nlp.pipeline.Annotation;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;
import edu.stanford.nlp.sentiment.SentimentCoreAnnotations;
import edu.stanford.nlp.trees.Tree;
import edu.stanford.nlp.util.CoreMap;

import org.ejml.*;


public class Mood {

	public static void main(String[] args) {
		//Set stderr to dev/null
		System.setErr(new PrintStream(new OutputStream() {
            public void write(int b) {
                //DO NOTHING
            }
        }));
		

		Properties props = new Properties();
		props.setProperty("annotators", "tokenize, ssplit, parse, sentiment");
		StanfordCoreNLP pipeline = new StanfordCoreNLP(props);

		//Text to evalutate
		String text = args[0];

		//Create an empty Annotation just with the given text
		Annotation document = new Annotation(text);

		//Run all Annotators on this text
		pipeline.annotate(document);

		List<CoreMap> sentences = document.get(SentencesAnnotation.class);

		//Sum of sentence scores
		int totalSum = 0;
		//get each sentence score
		for (CoreMap sentence : sentences) {
		  String s = sentence.get(SentimentCoreAnnotations.ClassName.class);
		  if(s.compareTo("Very positive") == 0)
			  totalSum += 5;
		  else if(s.compareTo("Positive") == 0)
			  totalSum += 4;
		  else if(s.compareTo("Neutral") == 0)
			  totalSum += 3;
		  else if(s.compareTo("Negative") == 0)
			  totalSum += 2;
		  else
			  totalSum += 1;
		}
		//print out average score
		System.out.println((int) Math.round(totalSum / sentences.size()));
	}

}

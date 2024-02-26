# coding=utf-8
# by Tiago Oliveira
# 26/02/2024

def calculate_wer(reference, hypothesis):
	ref_words = reference.split()
	hyp_words = hypothesis.split()
	# Counting the number of substitutions, deletions, and insertions
	substitutions = sum(1 for ref, hyp in zip(ref_words, hyp_words) if ref != hyp)
	deletions = len(ref_words) - len(hyp_words)
	insertions = len(hyp_words) - len(ref_words)
	# Total number of words in the reference text
	total_words = len(ref_words)
	# Calculating the Word Error Rate (WER)
	wer = (substitutions + deletions + insertions) / total_words
	return wer

reference_text = "The cat is sleeping on the mat."
hypothesis_text = "The cat is playing on mat."

#maybe adding calculator with files

if __name__ == "__main__":
    wer_score = calculate_wer(reference_text, hypothesis_text)
    print("Word Error Rate (WER):", wer_score)
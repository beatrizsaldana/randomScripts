# Script that will merge the X and Y chromosome of VCFs separated by chromosome (like the 1KGP VCFs)
# Check script before using

use strict;
use warnings;
use Data::Dumper;

my $vcf1 = $ARGV[0];
my $vcf2 = $ARGV[1];
my $outfile = $ARGV[2];


my @vcf1_samples;
my @vcf2_samples;
my @mapped_samples;

open(OUT, "+>", $outfile);

open(VCF1, $vcf1) or die "Could not open $vcf1\n";
while (<VCF1>)
{
	if ($_ =~ m/^#CHR/)
	{
		print OUT $_;
		
		$_ =~ s/\n//g;
		$_ =~ s/\r//g;

		my @line = split (/\t/,$_);

		for (my $i=0; $i < scalar @line; $i++)
		{
			push @vcf1_samples, $line[$i];
		}
	}
	else
	{
		print OUT $_;
	}
}

open(VCF2, $vcf2) or die "Could not open $vcf2\n";
while (<VCF2>)
{
	if ($_ =~ m/^##/)
	{
		next;
	}
	elsif ($_ =~ m/^#CHR/)
	{
		$_ =~ s/\n//g;
		$_ =~ s/\r//g;

		my @line = split (/\t/,$_);

		for (my $i = 0; $i < scalar @vcf1_samples; $i++)
		{
			my $checker = 0;
			for (my $j = 0; $j < scalar @line; $j++)
			{
				if($vcf1_samples[$i] eq $line[$j])
				{
					push @mapped_samples, $j;
					my $checker = 1;
					last;
				}
			}
			if($checker == 0)
			{
				push @mapped_samples, "N";
			}
		}
	}
	else
	{
		print OUT "\n";
		
		$_ =~ s/\n//g;
		$_ =~ s/\r//g;

		my @line = split (/\t/,$_);

		for (my $i = 0; $i < scalar @mapped_samples; $i++)
		{
			my $map = $mapped_samples[$i];
			if ($map ~ m/[0-9]/)
			{
				print OUT "$line[$map]\t";
			}
			if ($map eq "N")
			{
				print OUT ".|.\t"
			}
		}
	}
}

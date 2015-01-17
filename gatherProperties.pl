while (<>)
  {
	 if (/This is a word with property (\w+)/) {
		$mode = 0;
		$property = $1;
	 } elsif (/This is NOT a word with property (\w+)/) {
		$mode = 1;
		$property = $1;
	 } elsif (/\[/) {
		chomp;
		s/[\[\]' ]//g;
		my @words = split /,/;
		next if $#words > 0;
		push (@{$properties{$property}->[$mode]}, $words[0]);
	 }
  }

while (my ($property, $v) = each %properties)
  {
	 print "$property: " . join(',', @{$v->[0]}) . "\n";
	 print "NOT $property: " . join(',', @{$v->[1]}) . "\n";
  }

while (<>)
  {
	 if (/^===/) {
		%propertyMap = ();
	 } elsif (/This is a word with property (\w+)/) {
		$propertyMap{$1} = 0;
	 } elsif (/This is NOT a word with property (\w+)/) {
		$propertyMap{$1} = 1;
	 } elsif (/\[/) {
		chomp;
		s/[\[\]' ]//g;
		my @words = split /,/;
		next if $#words > 0;
		while (my ($p, $type) = each %propertyMap) {
		  push (@{$properties{$p}->[$type]}, $words[0]);
		}
	 }
  }

while (my ($property, $v) = each %properties)
  {
	 print "===\n$property\n===\n";
	 print join("\n", map(uc, @{$v->[0]})) . "\n";
	 print "===\nNOT $property\n===\n";
	 print join("\n", map(uc, @{$v->[1]})) . "\n";
  }

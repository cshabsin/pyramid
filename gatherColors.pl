while (<>)
  {
	 if (/^===/) {
		%propertyMap = ();
	 } elsif (/This word is associated with the color (\w+)/) {
		$propertyMap{$1} = 0;
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

while (my ($color, $v) = each %properties)
  {
	 print "===\n$color\n===\n";
	 print join("\n", map(uc, @{$v->[0]})) . "\n";
  }

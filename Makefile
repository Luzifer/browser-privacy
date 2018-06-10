default:

auto-hook-pre-commit:
	git status --porcelain | grep -q '^.M filters.txt' && python3 checksum.py || true
	git status --porcelain | grep -q '^M  filters.txt' && git add filters.txt || true

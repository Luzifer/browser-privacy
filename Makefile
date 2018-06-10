default:

auto-hook-pre-commit:
	python3 checksum.py
	git status --porcelain | grep -q '^M  filters.txt' && git add filters.txt || true

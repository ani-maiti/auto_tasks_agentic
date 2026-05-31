# Filter out non-archive files (assuming common archive extensions)
grep -E '\.(zip|rar|7z|tar\.gz|tgz|gz|bz2)$' files.txt > archives.txt
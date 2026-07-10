%global tl_name bidihl
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1c
Release:	%{tl_revision}.1
Summary:	Experimental bidi-aware text highlighting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/bidihl
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bidihl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bidihl.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Experimental bidi-aware text highlighting.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/xelatex
%dir %{_datadir}/texmf-dist/tex/xelatex
%dir %{_datadir}/texmf-dist/doc/xelatex/bidihl
%dir %{_datadir}/texmf-dist/tex/xelatex/bidihl
%doc %{_datadir}/texmf-dist/doc/xelatex/bidihl/README
%doc %{_datadir}/texmf-dist/doc/xelatex/bidihl/bidihl-doc.pdf
%doc %{_datadir}/texmf-dist/doc/xelatex/bidihl/bidihl-doc.tex
%doc %{_datadir}/texmf-dist/doc/xelatex/bidihl/test-bidihl.pdf
%doc %{_datadir}/texmf-dist/doc/xelatex/bidihl/test-bidihl.tex
%{_datadir}/texmf-dist/tex/xelatex/bidihl/bidihl.sty

Name:		texlive-gammas
Version:	56403
Release:	2
Summary:	Template for the GAMM Archive for Students
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gammas
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gammas.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gammas.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is the official document class for typesetting journal
articles for GAMM Archive for Students (GAMMAS), the
open-access online yournal run by the GAMM Juniors (GAMM =
Gesellschaft fur angewandte Mathematik und Mechanik).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/gammas
%{_texmfdistdir}/bibtex/bst/gammas
%doc %{_texmfdistdir}/doc/latex/gammas

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

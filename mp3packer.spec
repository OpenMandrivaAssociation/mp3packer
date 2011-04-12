%define name mp3packer
%define version 1.21
%define release %mkrel 1

Summary: MP3 reorganizer and repacker
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://omion.dyndns.org/mp3packer/%{name}-%{version}_src.zip
License: GPLv2+
Group: Sound
Url: http://omion.dyndns.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: ocaml

%description
MP3packer is a program which can rearrange the data within an MP3 to
fulfill specific goals. By default, the program generates the smallest
MP3 possible (with the least padding). However, many people also use
it to turn VBR files into CBR for use with players which don't support
VBR.

%prep
%setup -q -c

%build
%make OBJ_EXT=.o EXE_EXT=""

%install
rm -rf %{buildroot}
mkdir -p %buildroot%_bindir/
cp %name %buildroot%_bindir/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.html
%_bindir/%name

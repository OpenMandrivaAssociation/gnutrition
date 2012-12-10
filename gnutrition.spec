Name:		gnutrition
Summary:	A free nutrition analysis software
Version:	0.31
Release:	%mkrel 1
Source0:	http://ftp.gnu.org/gnu/gnutrition/%{name}-%{version}.tar.gz
Patch0:		gnutrition-0.31-mdv-fix-desktopfile-install-path.patch
URL:		http://www.gnu.org/software/gnutrition/
Group:		Sciences/Biology 
License:	GPLv3
BuildRequires:	pygtk2.0-devel
BuildRequires:	python-mysql
Requires:	gnome-python-desktop
Requires:	pygtk2.0
Requires:	python-mysql

%description
Gnutrition is a free nutrition analysis software written for the GNU
operating system. The US Department of Agriculture Nutrient Database of
Standard Reference is used as the source of food nutrient information.
It contains data on 81 nutrients for over 5,000 foods.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README ChangeLog
%{_bindir}/%{name}
%{_datadir}/%name/src/*
%{_datadir}/pixmaps/*.png
%{_datadir}/data/*.txt
%{_datadir}/gnome/apps/Applications/%{name}.desktop


%changelog
* Sat Jul 10 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.31-1mdv2011.0
+ Revision: 550207
- import gnutrition



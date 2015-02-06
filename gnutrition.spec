Summary:	A free nutrition analysis software
Name:		gnutrition
Version:	0.31
Release:	3
License:	GPLv3+
Group:		Sciences/Biology
Url:		http://www.gnu.org/software/gnutrition/
Source0:	http://ftp.gnu.org/gnu/gnutrition/%{name}-%{version}.tar.gz
Patch0:		gnutrition-0.31-mdv-fix-desktopfile-install-path.patch
BuildRequires:	python-mysql
BuildRequires:	pkgconfig(pygtk-2.0)
Requires:	gnome-python-desktop
Requires:	pygtk2.0
Requires:	python-mysql
BuildArch:	noarch

%description
Gnutrition is a free nutrition analysis software written for the GNU
operating system. The US Department of Agriculture Nutrient Database of
Standard Reference is used as the source of food nutrient information.
It contains data on 81 nutrients for over 5,000 foods.

%files
%doc AUTHORS COPYING README ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}/src/*
%{_datadir}/pixmaps/*.png
%{_datadir}/data/*.txt
%{_datadir}/gnome/apps/Applications/%{name}.desktop

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
%makeinstall


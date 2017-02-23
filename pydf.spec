%global srcname pydf

Name:           %{srcname}
Version:        12
Release:        1%{?dist}
Summary:        Fully colorized df clone written in python
Group:          Applications/System

License:        Public Domain
URL:            https://pypi.python.org/pypi/%{srcname}/%{version}
Source0:        http://kassiopeia.juls.savba.sk/~garabik/software/%{srcname}/%{name}_%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%description
pydf displays the amount of used and available space on your file systems,
just like df, but in colors. The output format is completely customizable.

%prep
%autosetup -n %{srcname}-%{version}

# Change shebang in individual files
sed -i '1s=^#!\s*/usr/bin/\(python\|env python\)[0-9.]*=#!%{__python3}=' pydf

%build

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1
install -p -m 755 pydf %{buildroot}/%{_bindir}
install -p -m 644 pydf.1 %{buildroot}/%{_mandir}/man1


%files
%license COPYING
%doc README COPYING
%{_bindir}/pydf
%{_mandir}/man1/pydf.1*

%changelog
* Thu Feb 23 2017 Artem Goncharov <artem.goncharov@gmail.com> 12-1
- new package built with tito, Python3, version bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild


* Mon May 2 2011 Clint Savage <herlo@fedoraproject.org> 9-3
- Removing define and properly adding other docs

* Sun May 1 2011 Clint Savage <herlo@fedoraproject.org> 9-2
- Fixing minor packaging issues

* Fri Apr 29 2011 Clint Savage <herlo@fedoraproject.org> 9-1
- Initial package build

Name:		python-logfury
Version:	1.0.1
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/l/logfury/logfury-%{version}.tar.gz
Summary:	(Toolkit for responsible, low-boilerplate logging of library method calls,)
URL:		https://pypi.org/project/logfury/
License:	BSD
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildSystem:	python
BuildArch:	noarch

%patchlist
logfury-1.0.1-relax-deps.patch

%description
('Toolkit for responsible, low-boilerplate logging of library method calls',)

%files
%{py_sitedir}/logfury
%{py_sitedir}/logfury-*.*-info

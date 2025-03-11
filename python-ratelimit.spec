# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		ratelimit
%define		egg_name	ratelimit
%define		pypi_name	ratelimit
Summary:	A function decorator preventing a function from being called more often than that allowed
Name:		python-%{module}
Version:	2.2.1
Release:	5
License:	MIT
Group:		Libraries/Python
Source0:	https://github.com/tomasbasham/ratelimit/archive/refs/tags/v%{version}.tar.gz
# Source0-md5:	ef2e15527c4514751527157b588bb25e
URL:		https://github.com/tomasbasham/ratelimit
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%if %{with tests}
#BuildRequires:	python-
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
#BuildRequires:	python3-
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A function decorator preventing a function from being called more
often than that allowed.

%package -n python3-%{module}
Summary:	A function decorator preventing a function from being called more often than that allowed
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-%{module}
A function decorator preventing a function from being called more
often than that allowed.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

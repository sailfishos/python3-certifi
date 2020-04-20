Name:       python3-certifi
Summary:    Carefully curated collection of Root Certificates
Version:    2020.04.05.1
Release:    1
License:    MPL 2.0
URL:        https://pypi.org/project/certifi/
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.bz2
Requires:   python3-base
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Certifi is a carefully curated collection of Root Certificates for validating
the trustworthiness of SSL certificates while verifying the identity of TLS
hosts. It has been extracted from the Requests project.

%prep
%setup -q -n %{name}-%{version}/certifi

%build
%{py3_build}

%install
rm -rf %{buildroot}
%{py3_install}

%files
%defattr(-,root,root,-)
%{python3_sitearch}/certifi
%{python3_sitearch}/certifi-*.egg-info

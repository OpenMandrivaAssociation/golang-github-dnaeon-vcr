# Run tests in check section
%bcond_without check

%global goipath         github.com/dnaeon/go-vcr
%global commit          8b144be0744f013a1b44386058f1fcb3ba98177d

%global common_description %{expand:
Record and replay your HTTP interactions for fast, deterministic and accurate 
tests.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Record and replay your HTTP interactions for fast, deterministic and accurate tests 
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(gopkg.in/yaml.v2)

%if %{with check}
BuildRequires: golang(golang.org/x/net/context)
%endif

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git8b144be
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20180628git8b144be
- Bump to commit 8b144be0744f013a1b44386058f1fcb3ba98177d

* Mon Mar 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180416gitb68d362
- First package for Fedora


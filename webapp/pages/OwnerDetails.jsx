import React from 'react';
import {Link} from 'react-router';
import PropTypes from 'prop-types';

import AsyncPage from '../components/AsyncPage';
import {Breadcrumbs, CrumbLink} from '../components/Breadcrumbs';
import Content from '../components/Content';
import Header from '../components/Header';
import Sidebar from '../components/Sidebar';

export default class OwnerDetails extends AsyncPage {
  static contextTypes = {
    ...AsyncPage.contextTypes,
    repoList: PropTypes.arrayOf(PropTypes.object).isRequired
  };

  static childContextTypes = {
    ...AsyncPage.childContextTypes,
    ...OwnerDetails.contextTypes
  };

  getDefaultState(props, context) {
    let {ownerName} = props.params;
    let {repoList} = context;
    let state = super.getDefaultState(props, context);
    state.repoList = repoList.filter(r => r.owner_name === ownerName);
    return state;
  }

  getTitle() {
    let {ownerName} = this.props.params;
    return ownerName;
  }

  renderBody() {
    let {ownerName} = this.props.params;
    return (
      <div>
        <Sidebar params={this.props.params} />
        <Content>
          <Header>
            <Breadcrumbs>
              <CrumbLink to={`/${ownerName}`}>
                {ownerName}
              </CrumbLink>
            </Breadcrumbs>
          </Header>
          <ul>
            {this.state.repoList.map(repo => {
              return (
                <li key={repo.name}>
                  <Link to={`/${repo.owner_name}/${repo.name}`}>
                    {repo.name}
                  </Link>
                </li>
              );
            })}
          </ul>
        </Content>
      </div>
    );
  }
}
